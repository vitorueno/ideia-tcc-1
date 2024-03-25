import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios';

function App() {
  const [contador, setContador] = useState(0);

  async function fetchContador() {
    const response1 = await axios.get('http://localhost:3000/contador');
    const response2 = await axios.get('http://localhost:5000/contador');
    const response3 = await axios.get('http://localhost:5030/contador');

    const dados1 = response1.data[0]['contador'];
    const dados2 = response2.data[0]['contador'];
    const dados3 = response3.data[0]['contador'];

    if (dados1 == dados2 && dados1 == dados3) {
      setContador(dados1);
    } else if (dados1 == dados2 && dados1 != dados3) {
      setContador(dados1);
      await axios.put('http://localhost:5030/contador/1', { contador: dados1 });
    } else if (dados1 != dados2 && dados1 == dados3) {
      setContador(dados1);
      await axios.put('http://localhost:5030/contador/1', { contador: dados1 });
    } else if (dados1 != dados2 && dados1 != dado3) {
      setContador(NaN);
      console.log('erro');
    } else {
      setContador(dados2);
      await axios.put('http://localhost:3000/contador/1', { contador: dados2 });
    }
  }

  useEffect(() => {
    fetchContador();
  }, []);

  const incrementarContador = async () => {
    try {
      await axios.get(`http://localhost:3000/contador/1/inc`);
      await axios.get(`http://localhost:5000/contador/1/inc`);
      await axios.get(`http://localhost:5030/contador/1/inc`);
      fetchContador();
    } catch (error) {
      console.log(error);
    }
  };

  const decrementarContador = async () => {
    try {
      await axios.get(`http://localhost:3000/contador/1/dec`);
      await axios.get(`http://localhost:5000/contador/1/dec`);
      await axios.get(`http://localhost:5030/contador/1/dec`);
    } catch (error) {
      console.log(error);
    }
    fetchContador();
  };

  return (
    <>
      <div className="card">
        <>
          <h2>Contador: {contador}</h2>
        </>
        <button onClick={decrementarContador}>
          -
        </button>
        <button onClick={incrementarContador}>
          +
        </button>
      </div>
    </>
  )
}

export default App
