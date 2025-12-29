# ``WKInternalsNotes/_WKTargetedElementInfo/mediaAndLinkURLs``

メディアやリンクの URL を集合で返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSSet<NSURL *> *mediaAndLinkURLs;
```

## Default Value
`API::TargetedElementInfo::mediaAndLinkURLs()` 由来の集合。

## Discussion
`mediaAndLinkURLs()` から `NSURL` 化できたもののみ `NSSet` に追加して返す。

## References
- [`_WKTargetedElementInfo.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L52)
- [`_WKTargetedElementInfo.mm#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L167)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
