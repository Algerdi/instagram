import React, {useState, useEffect} from 'react';
import {Link, useParams} from "react-router-dom";
import api from "../axios/axios";

function User() {

  const [users, setUsers] = useState(null);
  const params = useParams();

  useEffect(() => {
    const apiUrl = `http://127.0.0.1:8000/users/`;
    api.get(apiUrl).then((response) => {
      setUsers(response.data);
      console.log(users)
    });
  }, []);

  if (!users) return <h1>Loading...</h1>;

  return (
    <div>

    </div>
  );
}


export default User