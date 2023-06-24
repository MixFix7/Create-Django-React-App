import { createBrowserRouter } from "react-router-dom";
import { Home } from "../Home/Home";
import axios from "axios";

const router = createBrowserRouter([
    {
        path: '/',
        element: <Home/>,
        loader: async ({request}) => {
            try {
                const response = await axios.get(`http://localhost:8000/api/f/${1}/`);
                return response.data
            
              } catch (error) {
                console.error(error);
                return null
              }
            }
      },    
        
])

export default router