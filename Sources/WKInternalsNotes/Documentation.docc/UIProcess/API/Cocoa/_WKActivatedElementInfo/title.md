# ``WKInternalsNotes/_WKActivatedElementInfo/title``

要素のタイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *title;
```

## Default Value
初期化時に渡されたタイトル。

## Discussion
初期化時に `_title` を設定し、getter で返す。

## References
- [`_WKActivatedElementInfo.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L46)
- [`_WKActivatedElementInfo.mm#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L176)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
