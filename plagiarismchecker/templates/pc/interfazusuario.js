// Ejemplo de componente React para subir documentos
import React, { useState } from 'react';
import axios from 'axios';

function PlagiarismDetector() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/detect', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setResults(response.data);
    } catch (error) {
      console.error('Error detecting plagiarism:', error);
    }
  };

  return (
    <div>
      <h1>Plagiarism Detector</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Submit</button>
      </form>
      {results && <div>{JSON.stringify(results)}</div>}
    </div>
  );
}

export default PlagiarismDetector;
