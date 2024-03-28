location_mapping = {
    "Poranki": 8,
    "Kankipadu": 5,
    "Benz Circle": 0,
    "Gannavaram": 2,
    "Rajarajeswari Peta": 9,
    "Gunadala": 4,
    "Gollapudi": 3,
    "Enikepadu": 1,
    "Vidhyadharpuram": 10,
    "Penamaluru": 7,
    "Payakapuram": 6
}
status_mapping = {
    "Resale": 2,
    "Under Construction": 3,
    "Ready to move": 1,
    "New": 0
}

direction_mapping = {
    "Not Mentioned": 0,
    "East": 1,
    "West": 3,
    "NorthEast": 2
}

property_type_mapping = {
    "Apartment": 0,
    "Independent Floor": 1,
    "Independent House": 2,
    "Residential Plot": 3
}
with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('Scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def predict(bed,bath,loc,size,status,face,Type):
    location = location_mapping[loc]
    st = status_mapping[status]
    direction = direction_mapping[fee]
    property = property_type_mapping[Type]

    input_data=np.array([bed,bath,loc,size,status,face,Type])

    input_df = scaler.transform(input_data)

    return model.predict(input_df)[0]
if__name__ == '__main__':
    st.header('House Price Prediction')

    bed = col1.st.slider('No of bedrooms', max_value=10, min_value=0, value=2)
    bath = col1.st.slider('No of bathrooms', max_value=10, min_value=0, value=2)
    loc = col1.st.slider('Select a Location', list(location_mappingmapping.keys()))
    size = col1.st.slider('Size of Sqft', max_value=10000, min_value=500, value=1000,step=250) 
    status = col1.st.slider('Select the status', list(status_mappingmapping.keys()))
    face = col1.st.slider('Select a Direction', list(direction_mappingmapping.keys()))
    Type = col1.st.slider('Select the type', list(property_type_mappingmapping.keys()))
    