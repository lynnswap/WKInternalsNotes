# ``WKInternalsNotes/WKWebViewConfiguration``

## Purpose
`WKWebViewConfiguration` の non-public category/extension（`WKPrivate` / `WKPrivateDeprecated` / class extension など）に定義されている API を、Overview と Default Value を含めて追跡可能な形でまとめる。

## Default Value Definition
- 原則: `WKWebViewConfiguration()` 直後（`processPool` / `websiteDataStore` などの lazy 初期化対象へ未アクセスの状態）
- 条件付きデフォルト:
  - SDK 依存（`linkedOnOrAfterSDKWithBehavior(...)`）
  - 端末条件（iOS の UI idiom など）
  - compile-time feature（`ENABLE(...)`）

## Enums
- ``WKInternalsNotes/_WKDragLiftDelay``
  - ドラッグ開始（lift）までの遅延
- ``WKInternalsNotes/_WKAttributionOverrideTesting``
  - Attribution のテスト用オーバーライド
- ``WKInternalsNotes/_WKContentSecurityPolicyModeForExtension``
  - Web Extension 向け CSP モード

## Topics

### WKPrivate

#### Available via Public API
- ``WKInternalsNotes/WKWebViewConfiguration/_showsSystemScreenTimeBlockingView``
- ``WKInternalsNotes/WKWebViewConfiguration/_markedTextInputEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_printsBackgrounds``
- ``WKInternalsNotes/WKWebViewConfiguration/_requiresUserActionForAudioPlayback``
- ``WKInternalsNotes/WKWebViewConfiguration/_requiresUserActionForVideoPlayback``
- ``WKInternalsNotes/WKWebViewConfiguration/_strongWebExtensionController``
- ``WKInternalsNotes/WKWebViewConfiguration/_weakWebExtensionController``
- ``WKInternalsNotes/WKWebViewConfiguration/_webExtensionController``

#### Related / Session / Extensions
- ``WKInternalsNotes/WKWebViewConfiguration/_relatedWebView``
- ``WKInternalsNotes/WKWebViewConfiguration/_webViewToCloneSessionStorageFrom``
- ``WKInternalsNotes/WKWebViewConfiguration/_groupIdentifier``
- ``WKInternalsNotes/WKWebViewConfiguration/_visitedLinkStore``
- ``WKInternalsNotes/WKWebViewConfiguration/_requiredWebExtensionBaseURL``
- ``WKInternalsNotes/WKWebViewConfiguration/_alternateWebViewForNavigationGestures``

#### Rendering / Page Behavior
- ``WKInternalsNotes/WKWebViewConfiguration/_respectsImageOrientation``
- ``WKInternalsNotes/WKWebViewConfiguration/_incrementalRenderingSuppressionTimeout``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowsJavaScriptMarkup``
- ``WKInternalsNotes/WKWebViewConfiguration/_convertsPositionStyleOnCopy``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowsMetaRefresh``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowUniversalAccessFromFileURLs``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowTopNavigationToDataURLs``
- ``WKInternalsNotes/WKWebViewConfiguration/_needsStorageAccessFromFileURLsQuirk``
- ``WKInternalsNotes/WKWebViewConfiguration/_mainContentUserGestureOverrideEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_invisibleAutoplayNotPermitted``
- ``WKInternalsNotes/WKWebViewConfiguration/_mediaDataLoadsAutomatically``
- ``WKInternalsNotes/WKWebViewConfiguration/_attachmentElementEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_attachmentWideLayoutEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_attachmentFileWrapperClass``
- ``WKInternalsNotes/WKWebViewConfiguration/_initialCapitalizationEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_waitsForPaintAfterViewDidMoveToWindow``
- ``WKInternalsNotes/WKWebViewConfiguration/_controlledByAutomation``
- ``WKInternalsNotes/WKWebViewConfiguration/_applicationManifest``
- ``WKInternalsNotes/WKWebViewConfiguration/_colorFilterEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_incompleteImageBorderEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_drawsBackground``
- ``WKInternalsNotes/WKWebViewConfiguration/_shouldDeferAsynchronousScriptsUntilAfterDocumentLoad``

#### Networking / Security
- ``WKInternalsNotes/WKWebViewConfiguration/_websiteDataStoreIfExists``
- ``WKInternalsNotes/WKWebViewConfiguration/_corsDisablingPatterns``
- ``WKInternalsNotes/WKWebViewConfiguration/_maskedURLSchemes``
- ``WKInternalsNotes/WKWebViewConfiguration/_crossOriginAccessControlCheckEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_loadsFromNetwork``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowedNetworkHosts``
- ``WKInternalsNotes/WKWebViewConfiguration/_loadsSubresources``
- ``WKInternalsNotes/WKWebViewConfiguration/_ignoresAppBoundDomains``
- ``WKInternalsNotes/WKWebViewConfiguration/_clientNavigationsRunAtForegroundPriority``
- ``WKInternalsNotes/WKWebViewConfiguration/_portsForUpgradingInsecureSchemeForTesting``
- ``WKInternalsNotes/WKWebViewConfiguration/_attributedBundleIdentifier``
- ``WKInternalsNotes/WKWebViewConfiguration/_shouldRelaxThirdPartyCookieBlocking``
- ``WKInternalsNotes/WKWebViewConfiguration/_contentSecurityPolicyModeForExtension``
- ``WKInternalsNotes/WKWebViewConfiguration/_overrideContentSecurityPolicy``

#### Testing / Internal
- ``WKInternalsNotes/WKWebViewConfiguration/_allowPostingLegacySynchronousMessages``
- ``WKInternalsNotes/WKWebViewConfiguration/_shouldSendConsoleLogsToUIProcessForTesting``

#### Media / Playback / Process
- ``WKInternalsNotes/WKWebViewConfiguration/_applePayEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_mediaContentTypesRequiringHardwareSupport``
- ``WKInternalsNotes/WKWebViewConfiguration/_legacyEncryptedMediaAPIEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowMediaContentTypesRequiringHardwareSupportAsFallback``
- ``WKInternalsNotes/WKWebViewConfiguration/_mediaCaptureEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_additionalSupportedImageTypes``
- ``WKInternalsNotes/WKWebViewConfiguration/_undoManagerAPIEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_processDisplayName``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowTestOnlyIPC``
- ``WKInternalsNotes/WKWebViewConfiguration/_delaysWebProcessLaunchUntilFirstLoad``
- ``WKInternalsNotes/WKWebViewConfiguration/_cpuLimit``
- ``WKInternalsNotes/WKWebViewConfiguration/_appHighlightsEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_multiRepresentationHEICInsertionEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_scrollToTextFragmentIndicatorEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_scrollToTextFragmentMarkingEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_sampledPageTopColorMaxDifference``
- ``WKInternalsNotes/WKWebViewConfiguration/_sampledPageTopColorMinHeight``

#### iOS-only
- ``WKInternalsNotes/WKWebViewConfiguration/_alwaysRunsAtForegroundPriority``
- ``WKInternalsNotes/WKWebViewConfiguration/_inlineMediaPlaybackRequiresPlaysInlineAttribute``
- ``WKInternalsNotes/WKWebViewConfiguration/_allowsInlineMediaPlaybackAfterFullscreen``
- ``WKInternalsNotes/WKWebViewConfiguration/_dragLiftDelay``
- ``WKInternalsNotes/WKWebViewConfiguration/_longPressActionsEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_systemPreviewEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_shouldDecidePolicyBeforeLoadingQuickLookPreview``
- ``WKInternalsNotes/WKWebViewConfiguration/_canShowWhileLocked``
- ``WKInternalsNotes/WKWebViewConfiguration/_clickInteractionDriverForTesting``
- ``WKInternalsNotes/WKWebViewConfiguration/_appInitiatedOverrideValueForTesting``

#### macOS-only
- ``WKInternalsNotes/WKWebViewConfiguration/_showsURLsInToolTips``
- ``WKInternalsNotes/WKWebViewConfiguration/_serviceControlsEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_imageControlsEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_contextMenuQRCodeDetectionEnabled``
- ``WKInternalsNotes/WKWebViewConfiguration/_requiresUserActionForEditingControlsManager``
- ``WKInternalsNotes/WKWebViewConfiguration/_pageGroup``

#### visionOS-only (reference)
- ``WKInternalsNotes/WKWebViewConfiguration/_gamepadAccessRequiresExplicitConsent``
- ``WKInternalsNotes/WKWebViewConfiguration/_cssTransformStyleSeparatedEnabled``

### WKPrivateDeprecated
- ``WKInternalsNotes/WKWebViewConfiguration/_textInteractionGesturesEnabled``

### Class Extension
- ``WKInternalsNotes/WKWebViewConfiguration/_applicationNameForDesktopUserAgent``
- ``WKInternalsNotes/WKWebViewConfiguration/_isValidCustomScheme(_:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-15 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h) |
