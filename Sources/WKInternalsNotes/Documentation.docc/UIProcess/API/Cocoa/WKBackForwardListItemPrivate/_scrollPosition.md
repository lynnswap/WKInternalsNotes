# ``WKInternalsNotes/WKBackForwardListItem/_scrollPosition``

履歴項目のメインフレームのスクロール位置を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGPoint _scrollPosition WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
基になる `WebBackForwardListItem` の `mainFrameState()->scrollPosition` の値。

## Discussion
`mainFrameState()->scrollPosition` を `CGPoint` に変換して返す。履歴項目に保存されたスクロール位置を参照する。

## References
- [`WKBackForwardListItemPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItemPrivate.h#L33)
- [`WKBackForwardListItem.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBackForwardListItem.mm#L87)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
