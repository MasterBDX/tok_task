import react from 'react';

import Navbar from './components/Layout/Nav/Nav';
import Footer from './components/Layout/Footer/Footer';
import Main from './components/Layout/Main/Main';

import './App.css';
function App() {
  return (
    <div className="App">
          <Navbar />
          <Main />
          <Footer />
    </div>
  );
}

export default App;
