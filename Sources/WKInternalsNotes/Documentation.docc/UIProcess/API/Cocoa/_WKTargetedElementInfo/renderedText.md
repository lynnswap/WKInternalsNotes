# ``WKInternalsNotes/_WKTargetedElementInfo/renderedText``

描画済みテキストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *renderedText;
```

## Default Value
`API::TargetedElementInfo::renderedText()` の値。

## Discussion
内部の `_info` から `renderedText()` を取得して `NSString` 化して返す。

## References
- [`_WKTargetedElementInfo.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L56)
- [`_WKTargetedElementInfo.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L108)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
