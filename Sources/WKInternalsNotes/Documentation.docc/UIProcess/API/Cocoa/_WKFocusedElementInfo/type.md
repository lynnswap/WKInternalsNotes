# ``WKInternalsNotes/_WKFocusedElementInfo/type``

フォーカスされた要素の入力タイプを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKInputType type;
```

## Default Value
`FocusedElementInformation::elementType` を `WKInputType` に変換した値。

## Discussion
初期化時に `WebKit::InputType` を `WKInputType` に変換して保持し、その値を返す。

## References
- [`_WKFocusedElementInfo.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFocusedElementInfo.h#L31)
- [`WKContentViewInteraction.mm#L994`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L994)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
