import combineReducers from 'redux'
import { SystemState, ActionTypes, SELECT_PLACE } from '../store/types'

const initialState: SystemState = {
    selectedPlace: 0
}

export function annotateWorldApp(
    state = initialState, 
    action: ActionTypes
): SystemState {
    switch (action.type)
    {
        case SELECT_PLACE:
            return {
                selectedPlace: action.placeId
            }
        default:
            return state
    }
}
