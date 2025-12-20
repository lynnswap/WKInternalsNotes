# ``WKInternalsNotes/WKModelView/preview``

ASVInlinePreview を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) ASVInlinePreview *preview;
```

## Default Value
プレビュー生成前は `nil`。

## Discussion
`createPreview` で `ASVInlinePreview` を生成した後に `_preview` を保持し、このプロパティで返す。

## References
- [`WKModelView.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.h#L48)
- [`WKModelView.mm#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.mm#L60)
- [`WKModelView.mm#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.mm#L129)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
