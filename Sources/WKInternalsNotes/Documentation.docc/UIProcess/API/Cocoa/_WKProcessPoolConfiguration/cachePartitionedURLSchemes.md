# ``WKInternalsNotes/_WKProcessPoolConfiguration/cachePartitionedURLSchemes``

キャッシュをパーティション分離する URL スキームを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray *cachePartitionedURLSchemes;
```

## Default Value
未設定時は空配列を返す。

## Discussion
getter は `cachePartitionedURLSchemes` のベクタを `NSArray` に変換して返し、setter は文字列配列を `Vector<String>` に変換して保持する。

## References
- [`_WKProcessPoolConfiguration.mm#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L176)
- [`_WKProcessPoolConfiguration.mm#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L181)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
