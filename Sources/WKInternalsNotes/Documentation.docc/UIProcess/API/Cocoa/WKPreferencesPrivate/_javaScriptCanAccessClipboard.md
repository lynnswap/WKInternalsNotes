# ``WKInternalsNotes/WKPreferences/_javaScriptCanAccessClipboard``

JavaScript Can Access Clipboard を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setJavaScriptCanAccessClipboard:) BOOL _javaScriptCanAccessClipboard WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_javaScriptCanAccessClipboard = YES`: JavaScript Can Access Clipboard を有効化する。
- `_javaScriptCanAccessClipboard = NO`: JavaScript Can Access Clipboard を無効化する。
- Implementation: [`Source/WebCore/Modules/async-clipboard/Clipboard.cpp#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/async-clipboard/Clipboard.cpp#L58) で `javaScriptCanAccessClipboard()` が参照される。

## Details
- WebPreferences key: `JavaScriptCanAccessClipboard`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L128)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1346)
- [`Source/WebCore/Modules/async-clipboard/Clipboard.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/async-clipboard/Clipboard.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4182) (key: `JavaScriptCanAccessClipboard`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
