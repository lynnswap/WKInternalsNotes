# ``WKInternalsNotes/_WKTargetedElementInfo/searchableText``

検索用テキストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *searchableText;
```

## Default Value
`API::TargetedElementInfo::searchableText()` の値。

## Discussion
内部の `_info` から `searchableText()` を取得して `NSString` 化して返す。

## References
- [`_WKTargetedElementInfo.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L57)
- [`_WKTargetedElementInfo.mm#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L113)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
