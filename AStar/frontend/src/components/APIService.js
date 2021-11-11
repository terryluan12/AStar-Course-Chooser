export default class APIService {
    // Insert an article
  
    static InsertArticle(username, password) {
      console.log("im in insertarticle");
      return fetch(`http://localhost:5000/add`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        username: JSON.stringify(username),
        password: JSON.stringify(password)
      })
        .then((response) => response.json())
        .then(data => this.setState({userID: data.id}))
        .catch((error) => console.log(error));
    }

    static postQuery(query) {
      console.log("im in postQuery");
      return fetch(`http://localhost:5000/add`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        query: JSON.stringify(query)
      })
        .then((response) => response.json())
        .catch((error) => console.log(error));
    }

    
  }
  