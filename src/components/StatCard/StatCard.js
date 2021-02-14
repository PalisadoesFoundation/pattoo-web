/* React Imports */
import React from "react";
import PropTypes from 'prop-types';
import useBreakpoint from "../../hooks/useBreakpoint"

function StatCard({recentItems}) {
    const isStatic = useBreakpoint("md");
    return (
       <div className={`flex flex-col items-center rounded-md m-4 py-4 w-64 shadow-lg bg-white ${isStatic ? "" : "flex-grow"}`}>
            <p className="items-start font-bold text-xl text-blue-900 mb-4">Recently Updated</p>
            <div className={`flex flex-col ${isStatic ? "" : "items-stretch"}`}>
                {recentItems.map((items,index) => (
                    <p className="text-white font-bold items-center justify-center bg-blue-500 m-1 w-48 p-2 rounded-md text-center hover:bg-blue-800" key={index}>
                        {items}
                    </p>
                ))}
            </div>
       </div>
    );
}

export default StatCard;

StatCard.propTypes = {
    recentItems: PropTypes.array,
};