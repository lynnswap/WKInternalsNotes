# ``WKInternalsNotes/WKView``

## Topics

### Private

#### Properties
- ``WKInternalsNotes/WKView/_automaticallyAdjustsContentInsets``
- ``WKInternalsNotes/WKView/_backgroundColor``
- ``WKInternalsNotes/WKView/_fixedLayoutSize``
- ``WKInternalsNotes/WKView/_ignoresAllEvents``
- ``WKInternalsNotes/WKView/_ignoresNonWheelEvents``
- ``WKInternalsNotes/WKView/_inspectorAttachmentView``
- ``WKInternalsNotes/WKView/_layoutMode``
- ``WKInternalsNotes/WKView/_mediaPlaybackControlsView``
- ``WKInternalsNotes/WKView/_overlayScrollbarStyle``
- ``WKInternalsNotes/WKView/_overrideDeviceScaleFactor``
- ``WKInternalsNotes/WKView/_topContentInset``
- ``WKInternalsNotes/WKView/_totalHeightOfBanners``
- ``WKInternalsNotes/WKView/_useSystemAppearance``
- ``WKInternalsNotes/WKView/_viewScale``
- ``WKInternalsNotes/WKView/_wantsMediaPlaybackControlsView``
- ``WKInternalsNotes/WKView/allowsBackForwardNavigationGestures``
- ``WKInternalsNotes/WKView/allowsMagnification``
- ``WKInternalsNotes/WKView/magnification``
- ``WKInternalsNotes/WKView/minimumSizeForAutoLayout``
- ``WKInternalsNotes/WKView/pageRef``
- ``WKInternalsNotes/WKView/shouldClipToVisibleRect``
- ``WKInternalsNotes/WKView/shouldExpandToViewHeightForAutoLayout``
- ``WKInternalsNotes/WKView/sizeToContentAutoSizeMaximumSize``
- ``WKInternalsNotes/WKView/underlayColor``
- ``WKInternalsNotes/WKView/usingUISideCompositing``

#### Methods
- ``WKInternalsNotes/WKView/_addMediaPlaybackControlsView(_:)``
- ``WKInternalsNotes/WKView/_cancelImmediateActionAnimation()``
- ``WKInternalsNotes/WKView/_completeImmediateActionAnimation()``
- ``WKInternalsNotes/WKView/_didChangeContentSize(_:)``
- ``WKInternalsNotes/WKView/_dismissContentRelativeChildWindows()``
- ``WKInternalsNotes/WKView/_dismissContentRelativeChildWindowsWithAnimation(_:)``
- ``WKInternalsNotes/WKView/_doAfterNextPresentationUpdate(_:)``
- ``WKInternalsNotes/WKView/_gestureEventWasNotHandledByWebCore(_:)``
- ``WKInternalsNotes/WKView/_immediateActionAnimationControllerForHitTestResult(_:withType:userData:)``
- ``WKInternalsNotes/WKView/_prepareForImmediateActionAnimation()``
- ``WKInternalsNotes/WKView/_prepareForMoveToWindow(_:withCompletionHandler:)``
- ``WKInternalsNotes/WKView/_removeMediaPlaybackControlsView()``
- ``WKInternalsNotes/WKView/_setCustomSwipeViews(_:)``
- ``WKInternalsNotes/WKView/_setCustomSwipeViewsTopContentInset(_:)``
- ``WKInternalsNotes/WKView/_setDidMoveSwipeSnapshotCallback(_:)``
- ``WKInternalsNotes/WKView/_setShouldSuppressFirstResponderChanges(_:)``
- ``WKInternalsNotes/WKView/_simulateMouseMove(_:)``
- ``WKInternalsNotes/WKView/_tryToSwipeWithEvent(_:ignoringPinnedState:)``
- ``WKInternalsNotes/WKView/allowsLinkPreview()``
- ``WKInternalsNotes/WKView/beginDeferringViewInWindowChanges()``
- ``WKInternalsNotes/WKView/canChangeFrameLayout(_:)``
- ``WKInternalsNotes/WKView/createFullScreenWindow()``
- ``WKInternalsNotes/WKView/disableFrameSizeUpdates()``
- ``WKInternalsNotes/WKView/enableFrameSizeUpdates()``
- ``WKInternalsNotes/WKView/endDeferringViewInWindowChanges()``
- ``WKInternalsNotes/WKView/endDeferringViewInWindowChangesSync()``
- ``WKInternalsNotes/WKView/frameSizeUpdatesDisabled()``
- ``WKInternalsNotes/WKView/fullScreenPlaceholderView()``
- ``WKInternalsNotes/WKView/hideWordDefinitionWindow()``
- ``WKInternalsNotes/WKView/initWithFrame(_:configurationRef:)``
- ``WKInternalsNotes/WKView/initWithFrame(_:contextRef:pageGroupRef:)``
- ``WKInternalsNotes/WKView/initWithFrame(_:contextRef:pageGroupRef:relatedToPage:)``
- ``WKInternalsNotes/WKView/isDeferringViewInWindowChanges()``
- ``WKInternalsNotes/WKView/printOperationWithPrintInfo(_:forFrame:)``
- ``WKInternalsNotes/WKView/saveBackForwardSnapshotForCurrentItem()``
- ``WKInternalsNotes/WKView/saveBackForwardSnapshotForItem(_:)``
- ``WKInternalsNotes/WKView/setAllowsLinkPreview(_:)``
- ``WKInternalsNotes/WKView/setFrame(_:andScrollBy:)``
- ``WKInternalsNotes/WKView/setMagnification(_:centeredAtPoint:)``
- ``WKInternalsNotes/WKView/setWindowOcclusionDetectionEnabled(_:)``
- ``WKInternalsNotes/WKView/windowOcclusionDetectionEnabled()``

### PrivateForSubclassToDefine

- ``WKInternalsNotes/WKView/_shouldLoadIconWithParameters(_:completionHandler:)``

### Class Extension

- ``WKInternalsNotes/WKView/_thumbnailView``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`WKViewPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h) |
