import React, { useState, useEffect } from 'react';
import firebase from '../firebase';
import { collection, getDocs, getFirestore } from "firebase/firestore"; 


const Test = () => {

    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    const db = getFirestore(firebase);  
  
    useEffect(() => {

      const fetchData = async () => {
        setIsLoading(true);
        setError(null);
  
        try {
            const collectionRef = collection(db, "bank_statement");
            const querySnapshot = await getDocs(collectionRef);
            console.log("querySnapshot data",querySnapshot)
            const usersData = querySnapshot.docs.map(doc => doc.data());
            setData(usersData)

        } catch (error) {
            console.error('Error fetching data:', error);
            setError(error);

        } finally {
            setIsLoading(false);
        }
    };
  
      fetchData();
    }, []); // Empty dependency array ensures it runs only once on mount

    if (isLoading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>Error: {error.message}</p>;
    }


    return (
        <div className="main-container">
            <section className="height-100 bg-dark">
            <div className="container">
                <div className="row">
                <div className="col text-center">
                    <i className="icon-compass display-4" />
                    <h1 className="h2">Data from table</h1>
                    <table>
                        <thead>
                        <tr>
                            {/* Add table headers based on your data structure */}
                            <th>Field 1</th>
                            <th>Field 2</th>
                            {/* Add more headers as needed */}
                        </tr>
                        </thead>
                        <tbody>
                        {data.map((item, index) => (
                            <tr key={index}>
                            {/* Access and display data from each item in the data array */}
                            <td>{item.field1}</td>
                            <td>{item.field2}</td>
                            {/* Add more table cells for other fields */}
                            </tr>
                        ))}
                        </tbody>
                    </table>
                </div>
                </div>
            </div>
            </section>
        </div>
    );
}

export default Test;
