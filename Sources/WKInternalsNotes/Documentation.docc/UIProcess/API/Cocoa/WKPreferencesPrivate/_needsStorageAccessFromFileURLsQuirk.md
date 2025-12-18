# ``WKInternalsNotes/WKPreferences/_needsStorageAccessFromFileURLsQuirk``

Needs storage access from file URLs quirk を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNeedsStorageAccessFromFileURLsQuirk:) BOOL _needsStorageAccessFromFileURLsQuirk WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_needsStorageAccessFromFileURLsQuirk = YES`: Needs storage access from file URLs quirk を有効化する。
- `_needsStorageAccessFromFileURLsQuirk = NO`: Needs storage access from file URLs quirk を無効化する。
- Implementation: [`Document.cpp#L8359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L8359) の `SecurityOriginPolicy::create` が `needsStorageAccessFromFileURLsQuirk()` を参照する。

## Details
- WebPreferences key: `NeedsStorageAccessFromFileURLsQuirk`

## References
- [`WKPreferencesPrivate.h#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L230)
- [`WKPreferences.mm#L1239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1239)
- [`Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`UnifiedWebPreferences.yaml#L5590`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5590) (key: `NeedsStorageAccessFromFileURLsQuirk`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
