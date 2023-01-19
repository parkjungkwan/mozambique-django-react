import {useState} from "react"
import Pagination from "./admin/Pagination";


export default function Home(){

    const [currentPage, setCurrentPage] = useState(1);
  const lastPage = 3;

  return (
    <div className="page-container">
      <h1>React TypeScript Pagination</h1>
      <Pagination
        currentPage={currentPage}
        lastPage={lastPage}
        maxLength={7}
        setCurrentPage={setCurrentPage}
      />
    </div>
  );
}