export interface SystemState {
    selectedPlace: number
}

export const SELECT_PLACE = "SELECT_PLACE"
interface SelectPlaceAction {
    type: typeof SELECT_PLACE,
    placeId: number
}

export type ActionTypes = SelectPlaceAction