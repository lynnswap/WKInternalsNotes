# ``WKInternalsNotes/_WKActivatedElementInfo/imageURL``

要素に関連する画像 URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *imageURL;
```

## Default Value
`nil`（初期化時に設定される）。

## Discussion
初期化時に `InteractionInformationAtPosition` の `imageURL` を保持し、その値を返す。

## References
- [`_WKActivatedElementInfo.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L45)
- [`_WKActivatedElementInfo.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
