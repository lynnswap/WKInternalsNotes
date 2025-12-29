# ``WKInternalsNotes/_WKWebsiteDataSize/sizeOfDataTypes(_:)``

指定されたデータ種別の合計サイズを返す。

## Objective-C Declaration
```objective-c
- (unsigned long long)sizeOfDataTypes:(NSSet<NSString *> *)dataTypes;
```

## Discussion
`dataTypes` を `WebsiteDataType` に変換し、変換できた種別だけ `_size.typeSizes` から合算する。

## References
- [`_WKWebsiteDataSize.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataSize.h#L37)
- [`_WKWebsiteDataSize.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataSize.mm#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
