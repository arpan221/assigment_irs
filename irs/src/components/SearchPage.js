import React, { useState, useEffect } from 'react';
import SearchBar from './SearchBar';
import CountryList from './CountryList';

const SearchPage = (props) => {
  const [input, setInput] = useState('');
  const [countryListDefault, setCountryListDefault] = useState();
  const [countryList, setCountryList] = useState();

  const fetchData = async () => {
    return await fetch('http://127.0.0.1:8000/data/?value=%20Ammonium%20bicarbonate%20in%20a%20nice%20little%20.')
      .then(response => response.json())
      .then(data => {
         setCountryList(data)
         setCountryListDefault(data)
       });}

  const updateInput = async (input) => {
     const filtered = countryListDefault.filter(country => {
      return country.name.toLowerCase().includes(input.toLowerCase())
     })
     setInput(input);
     setCountryList(filtered);
  }

  useEffect( () => {fetchData()},[]);
  
  return (
    <>
      <h1>Products Review</h1>
      <SearchBar 
       input={input} 
       onChange={updateInput}
      />
      <CountryList countryList={countryList}/>
    </>
   );
}

export default SearchPage