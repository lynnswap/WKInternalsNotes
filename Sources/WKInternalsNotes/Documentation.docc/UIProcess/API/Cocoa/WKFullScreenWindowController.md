# ``WKInternalsNotes/WKFullScreenWindowController``

## Topics

### Properties (from WKFullScreenWindowController.h)

- ``WKInternalsNotes/WKFullScreenWindowController/finalFrame``
- ``WKInternalsNotes/WKFullScreenWindowController/initialFrame``
- ``WKInternalsNotes/WKFullScreenWindowController/savedConstraints``
- ``WKInternalsNotes/WKFullScreenWindowController/webViewPlaceholder``

### Methods (from WKFullScreenWindowController.h)

- ``WKInternalsNotes/WKFullScreenWindowController/beganEnterFullScreenWithInitialFrame(_:finalFrame:completionHandler:)``
- ``WKInternalsNotes/WKFullScreenWindowController/beganExitFullScreenWithInitialFrame(_:finalFrame:completionHandler:)``
- ``WKInternalsNotes/WKFullScreenWindowController/close()``
- ``WKInternalsNotes/WKFullScreenWindowController/enterFullScreen(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/exitFullScreen(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/exitFullScreenImmediately()``
- ``WKInternalsNotes/WKFullScreenWindowController/initWithWindow(_:webView:page:)``
- ``WKInternalsNotes/WKFullScreenWindowController/isFullScreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/requestExitFullScreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/videoControlsManagerDidChange()``

### Properties (from WKFullScreenWindowControllerIOS.h)

- ``WKInternalsNotes/WKFullScreenWindowController/fullScreenViewController``
- ``WKInternalsNotes/WKFullScreenWindowController/imageDimensions``
- ``WKInternalsNotes/WKFullScreenWindowController/isFullScreen``
- ``WKInternalsNotes/WKFullScreenWindowController/isUsingQuickLook``
- ``WKInternalsNotes/WKFullScreenWindowController/prefersSceneDimming``

### Methods (from WKFullScreenWindowControllerIOS.h)

- ``WKInternalsNotes/WKFullScreenWindowController/bestVideoFullscreenModeChanged()``
- ``WKInternalsNotes/WKFullScreenWindowController/didCleanupFullscreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/didEnterVideoFullscreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/didExitVideoFullscreen()``
- ``WKInternalsNotes/WKFullScreenWindowController/enterFullScreen(_:completionHandler:)``
- ``WKInternalsNotes/WKFullScreenWindowController/initWithWebView(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/requestRestoreFullScreen(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/resetSupportedOrientations()``
- ``WKInternalsNotes/WKFullScreenWindowController/setSupportedOrientations(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/toggleSceneDimming()``
- ``WKInternalsNotes/WKFullScreenWindowController/updateImageSource()``
- ``WKInternalsNotes/WKFullScreenWindowController/videosInElementFullscreenChanged()``
- ``WKInternalsNotes/WKFullScreenWindowController/webViewDidRemoveFromSuperviewWhileInFullscreen()``

### Properties

- ``WKInternalsNotes/WKFullScreenWindowController/_webView``
- ``WKInternalsNotes/WKFullScreenWindowController/logChannel``
- ``WKInternalsNotes/WKFullScreenWindowController/loggerPtr``
- ``WKInternalsNotes/WKFullScreenWindowController/logIdentifier``

### Methods

- ``WKInternalsNotes/WKFullScreenWindowController/_manager()``
- ``WKInternalsNotes/WKFullScreenWindowController/_protectedManager()``
- ``WKInternalsNotes/WKFullScreenWindowController/_replaceView(_:with:)``
- ``WKInternalsNotes/WKFullScreenWindowController/_startEnterFullScreenAnimationWithDuration(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/_startExitFullScreenAnimationWithDuration(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/didEnterPictureInPicture()``
- ``WKInternalsNotes/WKFullScreenWindowController/didExitPictureInPicture()``
- ``WKInternalsNotes/WKFullScreenWindowController/placeholderWillMoveToSuperview(_:)``
- ``WKInternalsNotes/WKFullScreenWindowController/previewWindowControllerDidClose(_:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
