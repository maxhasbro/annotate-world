import { ActionTypes, SELECT_PLACE } from "../store/types";

export function selectPlace(placeId: number): ActionTypes {
    return {
        type: SELECT_PLACE,
        placeId: placeId
    }
}