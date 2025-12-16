# ``WKInternalsNotes/WKPreferencesPrivate``

## Purpose
`WKPreferences` の private category（`WKPrivate` / `WKPrivateDeprecated`）に定義されている API を、Overview と Default Value を含めて追跡可能な形でまとめる。

## Default Value Definition
- 原則: `WKPreferences()` 直後（未変更）
- WebPreferences 由来の既定値は `Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml`（`WebKit` セクション）を根拠として記録する。

## Enums
- `_WKStorageBlockingPolicy`
  - ストレージブロッキングのポリシー
- `_WKDebugOverlayRegions`
  - Debug overlay の表示対象領域
- `_WKJavaScriptRuntimeFlags`
  - JavaScript runtime flags（現状は AllEnabled のみ）
- `_WKEditableLinkBehavior`
  - 編集可能領域でのリンク挙動
- `_WKPitchCorrectionAlgorithm`
  - pitch correction のアルゴリズム

## Topics

### Available via Public API
- ``WKInternalsNotes/WKPreferencesPrivate/_fullScreenEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_needsSiteSpecificQuirks``
- ``WKInternalsNotes/WKPreferencesPrivate/_overlayRegionsEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_safeBrowsingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_shouldPrintBackgrounds``

### WKPrivate
- ``WKInternalsNotes/WKPreferencesPrivate/_acceleratedCompositingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_acceleratedDrawingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_accessHandleEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_accessibilityIsolatedTreeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_allowFileAccessFromFileURLs``
- ``WKInternalsNotes/WKPreferencesPrivate/_allowPrivacySensitiveOperationsInNonPersistentDataStores``
- ``WKInternalsNotes/WKPreferencesPrivate/_allowsPictureInPictureMediaPlayback``
- ``WKInternalsNotes/WKPreferencesPrivate/_animatedImageAsyncDecodingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_appBadgeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_applePayCapabilityDisclosureAllowed``
- ``WKInternalsNotes/WKPreferencesPrivate/_avFoundationEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_colorFilterEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_compositingBordersVisible``
- ``WKInternalsNotes/WKPreferencesPrivate/_compositingRepaintCountersVisible``
- ``WKInternalsNotes/WKPreferencesPrivate/_contentChangeObserverEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_cssTransformStyleSeparatedEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_defaultFixedPitchFontSize``
- ``WKInternalsNotes/WKPreferencesPrivate/_defaultFontSize``
- ``WKInternalsNotes/WKPreferencesPrivate/_developerExtrasEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_deviceOrientationEventEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_diagnosticLoggingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_domPasteAllowed``
- ``WKInternalsNotes/WKPreferencesPrivate/_editableLinkBehavior``
- ``WKInternalsNotes/WKPreferencesPrivate/_enumeratingAllNetworkInterfacesEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_extensibleSSOEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_fileSystemAccessEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_fixedPitchFontFamily``
- ``WKInternalsNotes/WKPreferencesPrivate/_getUserMediaRequiresFocus``
- ``WKInternalsNotes/WKPreferencesPrivate/_hiddenPageDOMTimerThrottlingAutoIncreases``
- ``WKInternalsNotes/WKPreferencesPrivate/_hiddenPageDOMTimerThrottlingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_iceCandidateFilteringEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_inactiveMediaCaptureStreamRepromptIntervalInMinutes``
- ``WKInternalsNotes/WKPreferencesPrivate/_inactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes``
- ``WKInternalsNotes/WKPreferencesPrivate/_interactionRegionInlinePadding``
- ``WKInternalsNotes/WKPreferencesPrivate/_interactionRegionMinimumCornerRadius``
- ``WKInternalsNotes/WKPreferencesPrivate/_interruptAudioOnPageVisibilityChangeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_itpDebugModeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_javaScriptCanAccessClipboard``
- ``WKInternalsNotes/WKPreferencesPrivate/_javaScriptRuntimeFlags``
- ``WKInternalsNotes/WKPreferencesPrivate/_largeImageAsyncDecodingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_legacyLineLayoutVisualCoverageEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_loadsImagesAutomatically``
- ``WKInternalsNotes/WKPreferencesPrivate/_logsPageMessagesToSystemConsoleEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_lowPowerVideoAudioBufferSizeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_managedMediaSourceEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_managedMediaSourceHighThreshold``
- ``WKInternalsNotes/WKPreferencesPrivate/_managedMediaSourceLowThreshold``
- ``WKInternalsNotes/WKPreferencesPrivate/_mediaCapabilityGrantsEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_mediaCaptureRequiresSecureConnection``
- ``WKInternalsNotes/WKPreferencesPrivate/_mediaDevicesEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_mediaPreferredFullscreenWidth``
- ``WKInternalsNotes/WKPreferencesPrivate/_mediaSessionEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_mediaSourceEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_mockCaptureDevicesEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_mockCaptureDevicesPromptEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_modelDocumentEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_modelElementEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_modelNoPortalAttributeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_modelProcessEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_needsInAppBrowserPrivacyQuirks``
- ``WKInternalsNotes/WKPreferencesPrivate/_notificationEventEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_notificationsEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_pageVisibilityBasedProcessSuppressionEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_peerConnectionEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_pitchCorrectionAlgorithm``
- ``WKInternalsNotes/WKPreferencesPrivate/_privateClickMeasurementDebugModeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_privateClickMeasurementEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_punchOutWhiteBackgroundsInDarkMode``
- ``WKInternalsNotes/WKPreferencesPrivate/_pushAPIEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_remotePlaybackEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_requiresFullscreenToLockScreenOrientation``
- ``WKInternalsNotes/WKPreferencesPrivate/_requiresPageVisibilityForVideoToBeNowPlayingForTesting``
- ``WKInternalsNotes/WKPreferencesPrivate/_requiresPageVisibilityToPlayAudio``
- ``WKInternalsNotes/WKPreferencesPrivate/_resourceUsageOverlayVisible``
- ``WKInternalsNotes/WKPreferencesPrivate/_screenCaptureEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_secureContextChecksEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_serviceWorkerEntitlementDisabledForTesting``
- ``WKInternalsNotes/WKPreferencesPrivate/_shouldAllowUserInstalledFonts``
- ``WKInternalsNotes/WKPreferencesPrivate/_shouldEnableTextAutosizingBoost``
- ``WKInternalsNotes/WKPreferencesPrivate/_shouldIgnoreMetaViewport``
- ``WKInternalsNotes/WKPreferencesPrivate/_shouldSuppressKeyboardInputDuringProvisionalNavigation``
- ``WKInternalsNotes/WKPreferencesPrivate/_siteIsolationEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_speechRecognitionEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_standalone``
- ``WKInternalsNotes/WKPreferencesPrivate/_storageAPIEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_storageBlockingPolicy``
- ``WKInternalsNotes/WKPreferencesPrivate/_telephoneNumberDetectionIsEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_textAutosizingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_textExtractionEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_tiledScrollingIndicatorVisible``
- ``WKInternalsNotes/WKPreferencesPrivate/_updateSceneGeometryEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_verifyWindowOpenUserGestureFromUIProcess``
- ``WKInternalsNotes/WKPreferencesPrivate/_videoFullscreenRequiresElementFullscreen``
- ``WKInternalsNotes/WKPreferencesPrivate/_videoQualityIncludesDisplayCompositingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_visibleDebugOverlayRegions``
- ``WKInternalsNotes/WKPreferencesPrivate/_webAudioEnabled``


### macOS-only（#if !TARGET_OS_IPHONE）
- ``WKInternalsNotes/WKPreferencesPrivate/_aggressiveTileRetentionEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_allowsInlineMediaPlayback``
- ``WKInternalsNotes/WKPreferencesPrivate/_appNapEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_applePayEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_authorAndUserStylesEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_backspaceKeyNavigationEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_canvasUsesAcceleratedDrawing``
- ``WKInternalsNotes/WKPreferencesPrivate/_cookieEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_defaultTextEncodingName``
- ``WKInternalsNotes/WKPreferencesPrivate/_domTimersThrottlingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_inlineMediaPlaybackRequiresPlaysInlineAttribute``
- ``WKInternalsNotes/WKPreferencesPrivate/_invisibleMediaAutoplayNotPermitted``
- ``WKInternalsNotes/WKPreferencesPrivate/_legacyEncryptedMediaAPIEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_localFileContentSniffingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_mainContentUserGestureOverrideEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_needsStorageAccessFromFileURLsQuirk``
- ``WKInternalsNotes/WKPreferencesPrivate/_pdfPluginEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_requiresUserGestureForAudioPlayback``
- ``WKInternalsNotes/WKPreferencesPrivate/_requiresUserGestureForVideoPlayback``
- ``WKInternalsNotes/WKPreferencesPrivate/_serviceControlsEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_showsToolTipOverTruncatedText``
- ``WKInternalsNotes/WKPreferencesPrivate/_standardFontFamily``
- ``WKInternalsNotes/WKPreferencesPrivate/_suppressesIncrementalRendering``
- ``WKInternalsNotes/WKPreferencesPrivate/_textAreasAreResizable``
- ``WKInternalsNotes/WKPreferencesPrivate/_topNavigationToDataURLsAllowed``
- ``WKInternalsNotes/WKPreferencesPrivate/_universalAccessFromFileURLsAllowed``
- ``WKInternalsNotes/WKPreferencesPrivate/_useGiantTiles``
- ``WKInternalsNotes/WKPreferencesPrivate/_usesPageCache``
- ``WKInternalsNotes/WKPreferencesPrivate/_viewGestureDebuggingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_wantsBalancedSetDefersLoadingBehavior``
- ``WKInternalsNotes/WKPreferencesPrivate/_webArchiveDebugModeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_webGLEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_webSecurityEnabled``


### WKPrivateDeprecated
- ``WKInternalsNotes/WKPreferencesPrivate/_clientBadgeEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_displayListDrawingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_mediaStreamEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_offlineApplicationCacheIsEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_requestAnimationFrameEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_shouldAllowDesignSystemUIFonts``
- ``WKInternalsNotes/WKPreferencesPrivate/_subpixelAntialiasedLayerTextEnabled``


### WKPrivateDeprecated macOS-only（#if !TARGET_OS_IPHONE）
- ``WKInternalsNotes/WKPreferencesPrivate/_artificialPluginInitializationDelayEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_asynchronousPluginInitializationEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_dnsPrefetchingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_experimentalPlugInSandboxProfilesEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_pageCacheSupportsPlugins``
- ``WKInternalsNotes/WKPreferencesPrivate/_plugInSnapshottingEnabled``
- ``WKInternalsNotes/WKPreferencesPrivate/_subpixelCSSOMElementMetricsEnabled``


### Methods
- ``WKInternalsNotes/WKPreferencesPrivate/_disableMediaPlaybackRelatedFeatures()``
- ``WKInternalsNotes/WKPreferencesPrivate/_disableRichJavaScriptFeatures()``
- ``WKInternalsNotes/WKPreferencesPrivate/_experimentalFeatures()``
- ``WKInternalsNotes/WKPreferencesPrivate/_features()``
- ``WKInternalsNotes/WKPreferencesPrivate/_internalDebugFeatures()``
- ``WKInternalsNotes/WKPreferencesPrivate/_isEnabledForExperimentalFeature(_:)``
- ``WKInternalsNotes/WKPreferencesPrivate/_isEnabledForFeature(_:)``
- ``WKInternalsNotes/WKPreferencesPrivate/_isEnabledForInternalDebugFeature(_:)``
- ``WKInternalsNotes/WKPreferencesPrivate/_setEnabled(_:forExperimentalFeature:)``
- ``WKInternalsNotes/WKPreferencesPrivate/_setEnabled(_:forFeature:)``
- ``WKInternalsNotes/WKPreferencesPrivate/_setEnabled(_:forInternalDebugFeature:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-15 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h) |
