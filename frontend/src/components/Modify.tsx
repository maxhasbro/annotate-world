import React from 'react';
import { RouteComponentProps } from 'react-router-dom';

interface ModifyProps { 
    route: string 
}
  
const Modify = ({match}: RouteComponentProps<ModifyProps> ) => (
    <div>
        <h1>This value is passed in: {match.params.route}</h1>
    </div>
)

export default Modify