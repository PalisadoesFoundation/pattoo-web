/* React Imports */
import React from "react";
import PropTypes from 'prop-types';

function DataCard({title, value, lastChecked, timespan}) {
    return (
       <div className="flex flex-col bg-white rounded-md shadow-lg p-4 m-4">
           <div className="flex justify-between">
               <p className="font-semibold text-xl text-blue-900">{title}</p>
               <p className="bg-blue-500 px-2 mx-2 rounded-md font-normal text-sm self-center text-white">{timespan}</p>
           </div>
           <p className="text-2xl font-semibold text-gray-700">{value}</p>
           <p className="text-md font-normal text-gray-600 self-end">{lastChecked}</p>
       </div>
    );
}
export default DataCard;

DataCard.propTypes = {
    title: PropTypes.string, 
    value: PropTypes.string, 
    lastChecked: PropTypes.string, 
    timespan: PropTypes.string,
};