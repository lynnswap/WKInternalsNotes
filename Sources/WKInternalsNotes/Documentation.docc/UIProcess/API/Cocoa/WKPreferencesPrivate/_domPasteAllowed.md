# ``WKInternalsNotes/WKPreferencesPrivate/_domPasteAllowed``

DOM Paste を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDOMPasteAllowed:) BOOL _domPasteAllowed WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_domPasteAllowed = YES`: DOM Paste を許可する。
- `_domPasteAllowed = NO`: DOM Paste を禁止する。
- Implementation: [`Source/WebCore/editing/EditorCommand.cpp#L1199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/editing/EditorCommand.cpp#L1199) の `UnlinkCommand::create` が `domPasteAllowed()` を参照する。

## Details
- WebPreferences key: `DOMPasteAllowed`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L129)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1356`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1356)
- [`Source/WebCore/editing/EditorCommand.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/editing/EditorCommand.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2171) (key: `DOMPasteAllowed`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
