/* React Imports */
import React, {useState} from "react";

/* Module imports */
import useBreakpoint from "../../hooks/useBreakpoint"
import Transition from "../../hooks/Transition"
import Sidebar from "../Sidebar/Sidebar";
import Header from "../Header/Header";
import DataCard from "../DataCard/DataCard";
import StatCard from "../StatCard/StatCard";
import GraphCard from "../GraphCard/GraphCard";

/* Importing Styles*/
import "../../styles/main.css";

function Dashboard() {
  //Dashboard Page
  const[isClosed, setClosed] = useState(false);
  const isStatic = useBreakpoint("md");

  return (

    //======================== Desktop or laptop ========================//
    <div className="flex bg-gray-200">
      <Transition show={(isStatic || !isClosed)} enter="transition-all duration-200" enterFrom="-ml-64" enterTo="ml-0" leave="transition-all duration-200" leaveTo="-ml-64">
        <Sidebar isStatic={isStatic} isClosed={isClosed} setClosed={setClosed} />
      </Transition>

    
      <Transition
        appear={true}
        show={!isStatic && !isClosed}
        enter="transition-opacity duration-300"
        enterFrom="opacity-0"
        enterTo="opacity-50"
        leave="transition-opacity duration-300"
        leaveFrom="opacity-5"
        leaveTo="opacity-0"
      >
        <div className="fixed inset-0 bg-black opacity-0"/>
      </Transition>

        <main id="main-content" className="flex flex-col flex-grow min-h-screen min-w-screen">

          <Header isStatic={isStatic} setClosed={setClosed} isClosed={isClosed} label={"Dashboard"} name={"Jason Gayle"} title={"Python Developer"} />
        
              <div>
                <div className="flex items-center flex-wrap">
                  <DataCard title={"Files Injested"} value={"296"} lastChecked={"18 hours ago"} timespan={"Daily"}/>
                  <DataCard title={"Tracked Datapoints"} value={"150"} lastChecked={"18 hours ago"} timespan={"Daily"}/>
                  <DataCard title={"Active Agents"} value={"25"} lastChecked={"18 hours ago"} timespan={"Daily"}/>
                  <DataCard title={"Running Processes"} value={"15"} lastChecked={"18 hours ago"} timespan={"Daily"}/>
                </div>

                <div className="flex items-center flex-wrap">
                  <StatCard recentItems={["Favorites", "Charts", "Agents"]}/>
                  <GraphCard />
                </div>




              </div>

        </main>
      
    </div>


     //=========================== Mobile ==============================//


  );
}

export default Dashboard;
