# ``WKInternalsNotes/WKPreferencesPrivate/_siteIsolationEnabled``

Site Isolation を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSiteIsolationEnabled:) BOOL _siteIsolationEnabled WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Default Value
iOS: `NO` / macOS: `NO` / visionOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_siteIsolationEnabled = YES`: frame tree を site 単位で分離し、subframe が別の WebProcess（remote frame）で実行されることがある（プロセス数が増える）。
- `_siteIsolationEnabled = NO`: frame tree は 1 つの WebProcess で実行される（remote frame を使わない）。

## Details
- WebPreferences key: `SiteIsolationEnabled`
- Search hint: `EnabledBy=SiteIsolationEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L204)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1739`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1739)
- [`Source/WebKit/UIProcess/BrowsingContextGroup.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/BrowsingContextGroup.cpp)
- [`Source/WebKit/UIProcess/FrameProcess.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/FrameProcess.cpp)
- [`Source/WebKit/UIProcess/WebFrameProxy.messages.in`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebFrameProxy.messages.in)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7420`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7420) (key: `SiteIsolationEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
