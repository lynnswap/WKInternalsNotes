# ``WKInternalsNotes/WKUIScrollEdgeEffect/internallyHidden``

内部要因による非表示状態を管理する。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isInternallyHidden) BOOL internallyHidden;
```

## Default Value
`_hiddenSources` が空のため初期値は `NO`。

## Discussion
setter は `Internal` ソースで `_setHidden:fromSource:` を呼び、getter は `_hiddenSources` が内部フラグを持つかを返す。

## References
- [`WKUIScrollEdgeEffect.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.h#L41)
- [`WKUIScrollEdgeEffect.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.mm#L79)
- [`WKUIScrollEdgeEffect.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.mm#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
