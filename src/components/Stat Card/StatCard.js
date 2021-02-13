/* React Imports */
import React from "react";

function StatCard() {
    return (
       <div className="flex flex-col items-center rounded-md m-4 p-4 w-64 h-64 shadow-lg bg-white">
            <p className="items-start font-bold text-xl text-blue-900">Recently Updated</p>
            <div className="px-6 py-4 text-white font-bold">
                <div className="bg-blue-500 m-2 w-48 p-2 rounded-md text-center">Favorites</div>
                <div className="bg-blue-500 m-2 w-48 p-2 rounded-md text-center">Charts</div>
                <div className="bg-blue-500 m-2 w-48 p-2 rounded-md text-center">Agents</div>
            </div>
       </div>
    );
}

export default StatCard;