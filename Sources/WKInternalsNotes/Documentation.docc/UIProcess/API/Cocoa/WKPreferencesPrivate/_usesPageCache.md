# ``WKInternalsNotes/WKPreferences/_usesPageCache``

Back Forward Cache を使用するかどうかを切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUsesPageCache:) BOOL _usesPageCache WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_usesPageCache = YES`: Back Forward Cache を使用する。
- `_usesPageCache = NO`: Back Forward Cache を使用しない。
- Implementation: [`Source/WebCore/history/BackForwardCache.cpp#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/history/BackForwardCache.cpp#L180) の `DiagnosticLoggingKeys::deniedByClientKey` が `usesBackForwardCache()` を参照する。

## Details
- WebPreferences key: `UsesBackForwardCache`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L214)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1069`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1069)
- [`Source/WebCore/history/BackForwardCache.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/history/BackForwardCache.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8484`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8484) (key: `UsesBackForwardCache`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
