/* React Imports */
import React, {useState} from "react";
import useBreakpoint from "../../hooks/useBreakpoint"
import Transition from "../../hooks/Transition"
/* Module imports */
import Sidebar from "../Sidebar/Sidebar";
import Header from "../Header/Header";

/* Importing Styles*/
import "../../styles/main.css";

function Dashboard() {
  //Dashboard Page
  const[isClosed, setClosed] = useState(false);
  const isStatic = useBreakpoint("sm");

  return (

    //======================== Desktop or laptop ========================//
    <div className="flex bg-gray-200">
      <Transition show={(isStatic || !isClosed)} enter="transition-all duration-900" enterFrom="-ml-64" enterTo="ml-0" leave="transition-all duration-500" leaveTo="-ml-64">
        <Sidebar isStatic={isStatic} isClosed={isClosed} setClosed={setClosed} />
      </Transition>

    
      <Transition
        appear={true}
        show={!isStatic && !isClosed}
        enter="transition-opacity duration-300"
        enterFrom="opacity-0"
        enterTo="opacity-5"
        leave="transition-opacity duration-300"
        leaveFrom="opacity-5"
        leaveTo="opacity-0"
      >
        <div className="fixed inset-0 bg-black opacity-0"/>
      </Transition>

        <main id="main-content" className="flex flex-col flex-grow min-h-screen">

          <Header isStatic={isStatic} setClosed={setClosed} isClosed={isClosed} label={"Dashboard"} name={"Jason Gayle"} title={"Python Developer"} />
        
              {/* <DataCard title={"Files Injested"} value={"296"} lastChecked={"18 hours ago"} timespan={"Daily"}/> */}
              <p className="text-white">yp</p>

        </main>
      
    </div>


     //=========================== Mobile ==============================//


  );
}

export default Dashboard;
