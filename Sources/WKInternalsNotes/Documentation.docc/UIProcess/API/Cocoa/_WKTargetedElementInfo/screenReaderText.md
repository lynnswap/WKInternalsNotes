# ``WKInternalsNotes/_WKTargetedElementInfo/screenReaderText``

スクリーンリーダー向けテキストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *screenReaderText;
```

## Default Value
`API::TargetedElementInfo::screenReaderText()` の値。

## Discussion
内部の `_info` から `screenReaderText()` を取得して `NSString` 化して返す。

## References
- [`_WKTargetedElementInfo.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L58)
- [`_WKTargetedElementInfo.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L118)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
