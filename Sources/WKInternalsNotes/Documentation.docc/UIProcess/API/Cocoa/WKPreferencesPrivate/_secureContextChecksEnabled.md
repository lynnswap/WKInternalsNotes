# ``WKInternalsNotes/WKPreferencesPrivate/_secureContextChecksEnabled``

Secure Context Checks を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSecureContextChecksEnabled:) BOOL _secureContextChecksEnabled WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_secureContextChecksEnabled = YES`: Secure Context Checks を有効化する。
- `_secureContextChecksEnabled = NO`: Secure Context Checks を無効化する。
- Implementation: [`Source/WebCore/dom/Document.cpp#L8519`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L8519) の `Document::isSecureContext` が `secureContextChecksEnabled()` を参照する。

## Details
- WebPreferences key: `SecureContextChecksEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L166)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L953`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L953)
- [`Source/WebCore/dom/Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6870`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6870) (key: `SecureContextChecksEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
