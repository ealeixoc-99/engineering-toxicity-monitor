import { act, render, fireEvent, cleanup } from '@testing-library/react';
import ReactTestUtils from 'react-dom/test-utils'
import App from './App';
import axios from "axios";
import React from 'react'

afterEach(async()=>{
  await cleanup();
});

test('Test to submit a form and get result - Integration Test + End To End Test', async () => {
  const { getByTestId  } = render(<App />);
  
  await act(async () => {
    const node = getByTestId('text-area-test');
    node.value = 'I hate you';
    await ReactTestUtils.Simulate.change(node);

    fireEvent.submit(getByTestId('form-test'));
    await new Promise((r) => setTimeout(r, 2000));
  });

  var toxicity = parseFloat(getByTestId('test-toxicity').textContent);
  expect(toxicity).toBeGreaterThan(0.8);
});

test('Test status code of Back - Communication Test', async () => {
  const res = axios.get("http://localhost:5000/index?sentence=I_hate_you");
  expect((await res).status).toBe(200);
});

test('Test communication between Front and Back to get data - Communication test + Unit Test', async () => {
  const res = axios.get("http://localhost:5000/index?sentence=I_hate_you");

  var data = (await res).data.message;
  var toxicity = data.toxicity[0];

  expect(toxicity).toBeGreaterThan(0.8);
});

test('Test to check the page at the beginning - Unit Test', async () => {
  const { getByTestId } = render(<App />); 

  expect(getByTestId('textAreaLabel')).toBeInTheDocument();
});

test('Test to check if the form submit - Unit Test', async () => {
  const { getByTestId, getByText  } = render(<App />);
  
  fireEvent.submit(getByTestId('form-test'));
  
  expect(getByText('Loading')).toBeInTheDocument();
});
