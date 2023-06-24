import { createBrowserRouter } from "react-router-dom";
import { Home } from "../Home/Home";
import axios from "axios";

const router = createBrowserRouter([
    {
        path: '/:id',
        element: <Home/>,
        loader: async ({params, request}) => {
            try {
                const response = await axios.get(`http://localhost:8000/api/f/${params.id}/`);
                return response.data
            
              } catch (error) {
                console.error(error);
                return null
              }
            }
        }
])

export default router