# ``WKInternalsNotes/WKWebViewConfigurationPrivate``

## Purpose
`WKWebViewConfiguration` の private category（`WKPrivate` / `WKPrivateDeprecated`）に定義されている API を、Overview と Default Value を含めて追跡可能な形でまとめる。

## Default Value Definition
- 原則: `WKWebViewConfiguration()` 直後（`processPool` / `websiteDataStore` などの lazy 初期化対象へ未アクセスの状態）
- 条件付きデフォルト:
  - SDK 依存（`linkedOnOrAfterSDKWithBehavior(...)`）
  - 端末条件（iOS の UI idiom など）
  - compile-time feature（`ENABLE(...)`）

## Enums
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_WKDragLiftDelay``
  - ドラッグ開始（lift）までの遅延
- `_WKAttributionOverrideTesting`
  - Attribution のテスト用オーバーライド
- `_WKContentSecurityPolicyModeForExtension`
  - Web Extension 向け CSP モード

## Topics

### Available via Public API
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_showsSystemScreenTimeBlockingView``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_markedTextInputEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_printsBackgrounds``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_requiresUserActionForAudioPlayback``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_requiresUserActionForVideoPlayback``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_strongWebExtensionController``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_weakWebExtensionController``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_webExtensionController``

### Related / Session / Extensions
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_relatedWebView``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_webViewToCloneSessionStorageFrom``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_groupIdentifier``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_visitedLinkStore``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_requiredWebExtensionBaseURL``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_alternateWebViewForNavigationGestures``

### Rendering / Page Behavior
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_respectsImageOrientation``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_incrementalRenderingSuppressionTimeout``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowsJavaScriptMarkup``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_convertsPositionStyleOnCopy``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowsMetaRefresh``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowUniversalAccessFromFileURLs``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowTopNavigationToDataURLs``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_needsStorageAccessFromFileURLsQuirk``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_mainContentUserGestureOverrideEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_invisibleAutoplayNotPermitted``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_mediaDataLoadsAutomatically``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_attachmentElementEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_attachmentWideLayoutEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_attachmentFileWrapperClass``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_initialCapitalizationEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_waitsForPaintAfterViewDidMoveToWindow``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_controlledByAutomation``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_applicationManifest``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_colorFilterEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_incompleteImageBorderEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_drawsBackground``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_shouldDeferAsynchronousScriptsUntilAfterDocumentLoad``

### Networking / Security
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_websiteDataStoreIfExists``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_corsDisablingPatterns``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_maskedURLSchemes``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_crossOriginAccessControlCheckEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_loadsFromNetwork``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowedNetworkHosts``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_loadsSubresources``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_ignoresAppBoundDomains``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_clientNavigationsRunAtForegroundPriority``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_portsForUpgradingInsecureSchemeForTesting``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_attributedBundleIdentifier``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_shouldRelaxThirdPartyCookieBlocking``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_contentSecurityPolicyModeForExtension``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_overrideContentSecurityPolicy``

### Testing / Internal
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowPostingLegacySynchronousMessages``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_shouldSendConsoleLogsToUIProcessForTesting``

### Media / Playback / Process
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_applePayEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_mediaContentTypesRequiringHardwareSupport``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_legacyEncryptedMediaAPIEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowMediaContentTypesRequiringHardwareSupportAsFallback``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_mediaCaptureEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_additionalSupportedImageTypes``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_undoManagerAPIEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_processDisplayName``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowTestOnlyIPC``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_delaysWebProcessLaunchUntilFirstLoad``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_cpuLimit``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_appHighlightsEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_multiRepresentationHEICInsertionEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_scrollToTextFragmentIndicatorEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_scrollToTextFragmentMarkingEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_sampledPageTopColorMaxDifference``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_sampledPageTopColorMinHeight``

### iOS-only
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_alwaysRunsAtForegroundPriority``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_inlineMediaPlaybackRequiresPlaysInlineAttribute``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowsInlineMediaPlaybackAfterFullscreen``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_dragLiftDelay``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_longPressActionsEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_systemPreviewEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_shouldDecidePolicyBeforeLoadingQuickLookPreview``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_canShowWhileLocked``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_clickInteractionDriverForTesting``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_appInitiatedOverrideValueForTesting``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_textInteractionGesturesEnabled``

### macOS-only
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_showsURLsInToolTips``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_serviceControlsEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_imageControlsEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_contextMenuQRCodeDetectionEnabled``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_requiresUserActionForEditingControlsManager``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_pageGroup``

### visionOS-only (reference)
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_gamepadAccessRequiresExplicitConsent``
- ``WKInternalsNotes/WKWebViewConfigurationPrivate/_cssTransformStyleSeparatedEnabled``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-15 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h) |
