# ``WKInternalsNotes/WKPreferences``

## Purpose
`WKPreferences` の non-public category/extension（`WKPrivate` / `WKPrivateDeprecated` / class extension など）に定義されている API を、Overview と Default Value を含めて追跡可能な形でまとめる。

## Default Value Definition
- 原則: `WKPreferences()` 直後（未変更）
- WebPreferences 由来の既定値は `Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml`（`WebKit` セクション）を根拠として記録する。

## Enums
- ``WKInternalsNotes/_WKStorageBlockingPolicy``
  - ストレージブロッキングのポリシー
- ``WKInternalsNotes/_WKDebugOverlayRegions``
  - Debug overlay の表示対象領域
- ``WKInternalsNotes/_WKJavaScriptRuntimeFlags``
  - JavaScript runtime flags（現状は AllEnabled のみ）
- ``WKInternalsNotes/_WKEditableLinkBehavior``
  - 編集可能領域でのリンク挙動
- ``WKInternalsNotes/_WKPitchCorrectionAlgorithm``
  - pitch correction のアルゴリズム

## Topics

### Available via Public API
- ``WKInternalsNotes/WKPreferences/_fullScreenEnabled``
- ``WKInternalsNotes/WKPreferences/_needsSiteSpecificQuirks``
- ``WKInternalsNotes/WKPreferences/_overlayRegionsEnabled``
- ``WKInternalsNotes/WKPreferences/_safeBrowsingEnabled``
- ``WKInternalsNotes/WKPreferences/_shouldPrintBackgrounds``

### WKPrivate
- ``WKInternalsNotes/WKPreferences/_acceleratedCompositingEnabled``
- ``WKInternalsNotes/WKPreferences/_acceleratedDrawingEnabled``
- ``WKInternalsNotes/WKPreferences/_accessHandleEnabled``
- ``WKInternalsNotes/WKPreferences/_accessibilityIsolatedTreeEnabled``
- ``WKInternalsNotes/WKPreferences/_allowFileAccessFromFileURLs``
- ``WKInternalsNotes/WKPreferences/_allowPrivacySensitiveOperationsInNonPersistentDataStores``
- ``WKInternalsNotes/WKPreferences/_allowsPictureInPictureMediaPlayback``
- ``WKInternalsNotes/WKPreferences/_animatedImageAsyncDecodingEnabled``
- ``WKInternalsNotes/WKPreferences/_appBadgeEnabled``
- ``WKInternalsNotes/WKPreferences/_applePayCapabilityDisclosureAllowed``
- ``WKInternalsNotes/WKPreferences/_avFoundationEnabled``
- ``WKInternalsNotes/WKPreferences/_colorFilterEnabled``
- ``WKInternalsNotes/WKPreferences/_compositingBordersVisible``
- ``WKInternalsNotes/WKPreferences/_compositingRepaintCountersVisible``
- ``WKInternalsNotes/WKPreferences/_contentChangeObserverEnabled``
- ``WKInternalsNotes/WKPreferences/_cssTransformStyleSeparatedEnabled``
- ``WKInternalsNotes/WKPreferences/_defaultFixedPitchFontSize``
- ``WKInternalsNotes/WKPreferences/_defaultFontSize``
- ``WKInternalsNotes/WKPreferences/_developerExtrasEnabled``
- ``WKInternalsNotes/WKPreferences/_deviceOrientationEventEnabled``
- ``WKInternalsNotes/WKPreferences/_diagnosticLoggingEnabled``
- ``WKInternalsNotes/WKPreferences/_domPasteAllowed``
- ``WKInternalsNotes/WKPreferences/_editableLinkBehavior``
- ``WKInternalsNotes/WKPreferences/_enumeratingAllNetworkInterfacesEnabled``
- ``WKInternalsNotes/WKPreferences/_extensibleSSOEnabled``
- ``WKInternalsNotes/WKPreferences/_fileSystemAccessEnabled``
- ``WKInternalsNotes/WKPreferences/_fixedPitchFontFamily``
- ``WKInternalsNotes/WKPreferences/_getUserMediaRequiresFocus``
- ``WKInternalsNotes/WKPreferences/_hiddenPageDOMTimerThrottlingAutoIncreases``
- ``WKInternalsNotes/WKPreferences/_hiddenPageDOMTimerThrottlingEnabled``
- ``WKInternalsNotes/WKPreferences/_iceCandidateFilteringEnabled``
- ``WKInternalsNotes/WKPreferences/_inactiveMediaCaptureStreamRepromptIntervalInMinutes``
- ``WKInternalsNotes/WKPreferences/_inactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes``
- ``WKInternalsNotes/WKPreferences/_interactionRegionInlinePadding``
- ``WKInternalsNotes/WKPreferences/_interactionRegionMinimumCornerRadius``
- ``WKInternalsNotes/WKPreferences/_interruptAudioOnPageVisibilityChangeEnabled``
- ``WKInternalsNotes/WKPreferences/_itpDebugModeEnabled``
- ``WKInternalsNotes/WKPreferences/_javaScriptCanAccessClipboard``
- ``WKInternalsNotes/WKPreferences/_javaScriptRuntimeFlags``
- ``WKInternalsNotes/WKPreferences/_largeImageAsyncDecodingEnabled``
- ``WKInternalsNotes/WKPreferences/_legacyLineLayoutVisualCoverageEnabled``
- ``WKInternalsNotes/WKPreferences/_loadsImagesAutomatically``
- ``WKInternalsNotes/WKPreferences/_logsPageMessagesToSystemConsoleEnabled``
- ``WKInternalsNotes/WKPreferences/_lowPowerVideoAudioBufferSizeEnabled``
- ``WKInternalsNotes/WKPreferences/_managedMediaSourceEnabled``
- ``WKInternalsNotes/WKPreferences/_managedMediaSourceHighThreshold``
- ``WKInternalsNotes/WKPreferences/_managedMediaSourceLowThreshold``
- ``WKInternalsNotes/WKPreferences/_mediaCapabilityGrantsEnabled``
- ``WKInternalsNotes/WKPreferences/_mediaCaptureRequiresSecureConnection``
- ``WKInternalsNotes/WKPreferences/_mediaDevicesEnabled``
- ``WKInternalsNotes/WKPreferences/_mediaPreferredFullscreenWidth``
- ``WKInternalsNotes/WKPreferences/_mediaSessionEnabled``
- ``WKInternalsNotes/WKPreferences/_mediaSourceEnabled``
- ``WKInternalsNotes/WKPreferences/_mockCaptureDevicesEnabled``
- ``WKInternalsNotes/WKPreferences/_mockCaptureDevicesPromptEnabled``
- ``WKInternalsNotes/WKPreferences/_modelDocumentEnabled``
- ``WKInternalsNotes/WKPreferences/_modelElementEnabled``
- ``WKInternalsNotes/WKPreferences/_modelNoPortalAttributeEnabled``
- ``WKInternalsNotes/WKPreferences/_modelProcessEnabled``
- ``WKInternalsNotes/WKPreferences/_needsInAppBrowserPrivacyQuirks``
- ``WKInternalsNotes/WKPreferences/_notificationEventEnabled``
- ``WKInternalsNotes/WKPreferences/_notificationsEnabled``
- ``WKInternalsNotes/WKPreferences/_pageVisibilityBasedProcessSuppressionEnabled``
- ``WKInternalsNotes/WKPreferences/_peerConnectionEnabled``
- ``WKInternalsNotes/WKPreferences/_pitchCorrectionAlgorithm``
- ``WKInternalsNotes/WKPreferences/_privateClickMeasurementDebugModeEnabled``
- ``WKInternalsNotes/WKPreferences/_privateClickMeasurementEnabled``
- ``WKInternalsNotes/WKPreferences/_punchOutWhiteBackgroundsInDarkMode``
- ``WKInternalsNotes/WKPreferences/_pushAPIEnabled``
- ``WKInternalsNotes/WKPreferences/_remotePlaybackEnabled``
- ``WKInternalsNotes/WKPreferences/_requiresFullscreenToLockScreenOrientation``
- ``WKInternalsNotes/WKPreferences/_requiresPageVisibilityForVideoToBeNowPlayingForTesting``
- ``WKInternalsNotes/WKPreferences/_requiresPageVisibilityToPlayAudio``
- ``WKInternalsNotes/WKPreferences/_resourceUsageOverlayVisible``
- ``WKInternalsNotes/WKPreferences/_screenCaptureEnabled``
- ``WKInternalsNotes/WKPreferences/_secureContextChecksEnabled``
- ``WKInternalsNotes/WKPreferences/_serviceWorkerEntitlementDisabledForTesting``
- ``WKInternalsNotes/WKPreferences/_shouldAllowUserInstalledFonts``
- ``WKInternalsNotes/WKPreferences/_shouldEnableTextAutosizingBoost``
- ``WKInternalsNotes/WKPreferences/_shouldIgnoreMetaViewport``
- ``WKInternalsNotes/WKPreferences/_shouldSuppressKeyboardInputDuringProvisionalNavigation``
- ``WKInternalsNotes/WKPreferences/_siteIsolationEnabled``
- ``WKInternalsNotes/WKPreferences/_speechRecognitionEnabled``
- ``WKInternalsNotes/WKPreferences/_standalone``
- ``WKInternalsNotes/WKPreferences/_storageAPIEnabled``
- ``WKInternalsNotes/WKPreferences/_storageBlockingPolicy``
- ``WKInternalsNotes/WKPreferences/_telephoneNumberDetectionIsEnabled``
- ``WKInternalsNotes/WKPreferences/_textAutosizingEnabled``
- ``WKInternalsNotes/WKPreferences/_textExtractionEnabled``
- ``WKInternalsNotes/WKPreferences/_tiledScrollingIndicatorVisible``
- ``WKInternalsNotes/WKPreferences/_verifyWindowOpenUserGestureFromUIProcess``
- ``WKInternalsNotes/WKPreferences/_videoFullscreenRequiresElementFullscreen``
- ``WKInternalsNotes/WKPreferences/_videoQualityIncludesDisplayCompositingEnabled``
- ``WKInternalsNotes/WKPreferences/_visibleDebugOverlayRegions``
- ``WKInternalsNotes/WKPreferences/_webAudioEnabled``


### macOS-only（#if !TARGET_OS_IPHONE）
- ``WKInternalsNotes/WKPreferences/_aggressiveTileRetentionEnabled``
- ``WKInternalsNotes/WKPreferences/_allowsInlineMediaPlayback``
- ``WKInternalsNotes/WKPreferences/_appNapEnabled``
- ``WKInternalsNotes/WKPreferences/_applePayEnabled``
- ``WKInternalsNotes/WKPreferences/_authorAndUserStylesEnabled``
- ``WKInternalsNotes/WKPreferences/_backspaceKeyNavigationEnabled``
- ``WKInternalsNotes/WKPreferences/_canvasUsesAcceleratedDrawing``
- ``WKInternalsNotes/WKPreferences/_cookieEnabled``
- ``WKInternalsNotes/WKPreferences/_defaultTextEncodingName``
- ``WKInternalsNotes/WKPreferences/_domTimersThrottlingEnabled``
- ``WKInternalsNotes/WKPreferences/_inlineMediaPlaybackRequiresPlaysInlineAttribute``
- ``WKInternalsNotes/WKPreferences/_invisibleMediaAutoplayNotPermitted``
- ``WKInternalsNotes/WKPreferences/_legacyEncryptedMediaAPIEnabled``
- ``WKInternalsNotes/WKPreferences/_localFileContentSniffingEnabled``
- ``WKInternalsNotes/WKPreferences/_mainContentUserGestureOverrideEnabled``
- ``WKInternalsNotes/WKPreferences/_needsStorageAccessFromFileURLsQuirk``
- ``WKInternalsNotes/WKPreferences/_pdfPluginEnabled``
- ``WKInternalsNotes/WKPreferences/_requiresUserGestureForAudioPlayback``
- ``WKInternalsNotes/WKPreferences/_requiresUserGestureForVideoPlayback``
- ``WKInternalsNotes/WKPreferences/_serviceControlsEnabled``
- ``WKInternalsNotes/WKPreferences/_showsToolTipOverTruncatedText``
- ``WKInternalsNotes/WKPreferences/_standardFontFamily``
- ``WKInternalsNotes/WKPreferences/_suppressesIncrementalRendering``
- ``WKInternalsNotes/WKPreferences/_textAreasAreResizable``
- ``WKInternalsNotes/WKPreferences/_topNavigationToDataURLsAllowed``
- ``WKInternalsNotes/WKPreferences/_universalAccessFromFileURLsAllowed``
- ``WKInternalsNotes/WKPreferences/_useGiantTiles``
- ``WKInternalsNotes/WKPreferences/_usesPageCache``
- ``WKInternalsNotes/WKPreferences/_viewGestureDebuggingEnabled``
- ``WKInternalsNotes/WKPreferences/_wantsBalancedSetDefersLoadingBehavior``
- ``WKInternalsNotes/WKPreferences/_webArchiveDebugModeEnabled``
- ``WKInternalsNotes/WKPreferences/_webGLEnabled``
- ``WKInternalsNotes/WKPreferences/_webSecurityEnabled``


### WKPrivateDeprecated
- ``WKInternalsNotes/WKPreferences/_clientBadgeEnabled``
- ``WKInternalsNotes/WKPreferences/_displayListDrawingEnabled``
- ``WKInternalsNotes/WKPreferences/_mediaStreamEnabled``
- ``WKInternalsNotes/WKPreferences/_offlineApplicationCacheIsEnabled``
- ``WKInternalsNotes/WKPreferences/_requestAnimationFrameEnabled``
- ``WKInternalsNotes/WKPreferences/_shouldAllowDesignSystemUIFonts``
- ``WKInternalsNotes/WKPreferences/_subpixelAntialiasedLayerTextEnabled``


### WKPrivateDeprecated macOS-only（#if !TARGET_OS_IPHONE）
- ``WKInternalsNotes/WKPreferences/_artificialPluginInitializationDelayEnabled``
- ``WKInternalsNotes/WKPreferences/_asynchronousPluginInitializationEnabled``
- ``WKInternalsNotes/WKPreferences/_dnsPrefetchingEnabled``
- ``WKInternalsNotes/WKPreferences/_experimentalPlugInSandboxProfilesEnabled``
- ``WKInternalsNotes/WKPreferences/_pageCacheSupportsPlugins``
- ``WKInternalsNotes/WKPreferences/_plugInSnapshottingEnabled``
- ``WKInternalsNotes/WKPreferences/_subpixelCSSOMElementMetricsEnabled``

### Class Extension
- ``WKInternalsNotes/WKPreferences/_useSystemAppearance``


### Methods
- ``WKInternalsNotes/WKPreferences/_disableMediaPlaybackRelatedFeatures()``
- ``WKInternalsNotes/WKPreferences/_disableRichJavaScriptFeatures()``
- ``WKInternalsNotes/WKPreferences/_experimentalFeatures()``
- ``WKInternalsNotes/WKPreferences/_features()``
- ``WKInternalsNotes/WKPreferences/_internalDebugFeatures()``
- ``WKInternalsNotes/WKPreferences/_isEnabledForExperimentalFeature(_:)``
- ``WKInternalsNotes/WKPreferences/_isEnabledForFeature(_:)``
- ``WKInternalsNotes/WKPreferences/_isEnabledForInternalDebugFeature(_:)``
- ``WKInternalsNotes/WKPreferences/_setEnabled(_:forExperimentalFeature:)``
- ``WKInternalsNotes/WKPreferences/_setEnabled(_:forFeature:)``
- ``WKInternalsNotes/WKPreferences/_setEnabled(_:forInternalDebugFeature:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-15 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`WKPreferencesPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h) |
