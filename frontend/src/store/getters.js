const getters = {
    language: state => state.app.language,
    device: state => state.app.device,
    docWidth: state => state.app.document_width,
    docHeight: state => state.app.document_height,
    channels: state => state.app.channels,
}
export default getters
