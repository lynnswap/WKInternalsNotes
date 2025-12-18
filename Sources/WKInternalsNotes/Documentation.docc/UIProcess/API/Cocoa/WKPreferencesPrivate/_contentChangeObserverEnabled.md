# ``WKInternalsNotes/WKPreferences/_contentChangeObserverEnabled``

Content Change Observer を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setContentChangeObserverEnabled:) BOOL _contentChangeObserverEnabled WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_contentChangeObserverEnabled = YES`: Content Change Observer を有効化する。
- `_contentChangeObserverEnabled = NO`: Content Change Observer を無効化する。
- Implementation: [`Source/WebCore/page/ios/ContentChangeObserver.cpp#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/ios/ContentChangeObserver.cpp#L85) の `ContentChangeObserver::isContentChangeObserverEnabled` が `contentChangeObserverEnabled()` を参照する。

## Details
- WebPreferences key: `ContentChangeObserverEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L81)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L376`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L376)
- [`Source/WebCore/page/ios/ContentChangeObserver.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/ios/ContentChangeObserver.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1921`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1921) (key: `ContentChangeObserverEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
