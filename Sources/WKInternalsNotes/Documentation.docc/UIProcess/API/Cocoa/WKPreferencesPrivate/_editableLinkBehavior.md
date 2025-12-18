# ``WKInternalsNotes/WKPreferences/_editableLinkBehavior``

Editable Link Behavior を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setEditableLinkBehavior:) _WKEditableLinkBehavior _editableLinkBehavior WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
iOS: `WebCore::EditableLinkBehavior::NeverLive` / macOS: `WebCore::EditableLinkBehavior::NeverLive`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_editableLinkBehavior` を設定すると: Editable Link Behavior を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/html/HTMLAnchorElement.cpp#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLAnchorElement.cpp#L199) の `HTMLAnchorElement::setActive` が `editableLinkBehavior()` を参照する。

## Details
- WebPreferences key: `EditableLinkBehavior`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L133)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L823`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L823)
- [`Source/WebCore/html/HTMLAnchorElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLAnchorElement.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2551`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2551) (key: `EditableLinkBehavior`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
