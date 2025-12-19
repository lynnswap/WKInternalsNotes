# ``WKInternalsNotes/WKFullScreenWindowController``

## Topics

### Logging

- ``WKInternalsNotes/WKFullScreenWindowController/logChannel``
- ``WKInternalsNotes/WKFullScreenWindowController/logIdentifier``
- ``WKInternalsNotes/WKFullScreenWindowController/loggerPtr``

### Private

- ``WKInternalsNotes/WKFullScreenWindowController/_manager()``
- ``WKInternalsNotes/WKFullScreenWindowController/_protectedManager()``
- ``WKInternalsNotes/WKFullScreenWindowController/_replaceView(_:with:)``
- ``WKInternalsNotes/WKFullScreenWindowController/_startEnterFullScreenAnimationWithDuration(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/_startExitFullScreenAnimationWithDuration(_:)``

### VideoPresentationManagerProxyClient

- ``WKInternalsNotes/WKFullScreenWindowController/didEnterPictureInPicture()``
- ``WKInternalsNotes/WKFullScreenWindowController/didEnterVideoFullscreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/didExitPictureInPicture()``
- ``WKInternalsNotes/WKFullScreenWindowController/didExitVideoFullscreen()``

### WKPreviewWindowControllerDelegate

- ``WKInternalsNotes/WKFullScreenWindowController/previewWindowControllerDidClose(_:)``

### Class Extension

#### Properties
- ``WKInternalsNotes/WKFullScreenWindowController/_webView``

#### Methods
- ``WKInternalsNotes/WKFullScreenWindowController/placeholderWillMoveToSuperview(_:)``

### Type

#### Properties
- ``WKInternalsNotes/WKFullScreenWindowController/finalFrame``
- ``WKInternalsNotes/WKFullScreenWindowController/fullScreenViewController``
- ``WKInternalsNotes/WKFullScreenWindowController/imageDimensions``
- ``WKInternalsNotes/WKFullScreenWindowController/initialFrame``
- ``WKInternalsNotes/WKFullScreenWindowController/isFullScreen``
- ``WKInternalsNotes/WKFullScreenWindowController/isUsingQuickLook``
- ``WKInternalsNotes/WKFullScreenWindowController/prefersSceneDimming``
- ``WKInternalsNotes/WKFullScreenWindowController/savedConstraints``
- ``WKInternalsNotes/WKFullScreenWindowController/webViewPlaceholder``

#### Methods
- ``WKInternalsNotes/WKFullScreenWindowController/beganEnterFullScreenWithInitialFrame(_:finalFrame:completionHandler:)``
- ``WKInternalsNotes/WKFullScreenWindowController/beganExitFullScreenWithInitialFrame(_:finalFrame:completionHandler:)``
- ``WKInternalsNotes/WKFullScreenWindowController/bestVideoFullscreenModeChanged()``
- ``WKInternalsNotes/WKFullScreenWindowController/close()``
- ``WKInternalsNotes/WKFullScreenWindowController/didCleanupFullscreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/didEnterVideoFullscreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/didExitVideoFullscreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/enterFullScreen(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/enterFullScreen(_:completionHandler:)``
- ``WKInternalsNotes/WKFullScreenWindowController/exitFullScreen(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/exitFullScreenImmediately()``
- ``WKInternalsNotes/WKFullScreenWindowController/initWithWebView(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/initWithWindow(_:webView:page:)``
- ``WKInternalsNotes/WKFullScreenWindowController/isFullScreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/requestExitFullScreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/requestRestoreFullScreen(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/resetSupportedOrientations()``
- ``WKInternalsNotes/WKFullScreenWindowController/setSupportedOrientations(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/toggleSceneDimming()``
- ``WKInternalsNotes/WKFullScreenWindowController/updateImageSource()``
- ``WKInternalsNotes/WKFullScreenWindowController/videoControlsManagerDidChange()``
- ``WKInternalsNotes/WKFullScreenWindowController/videosInElementFullscreenChanged()``
- ``WKInternalsNotes/WKFullScreenWindowController/webViewDidRemoveFromSuperviewWhileInFullscreen()``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
