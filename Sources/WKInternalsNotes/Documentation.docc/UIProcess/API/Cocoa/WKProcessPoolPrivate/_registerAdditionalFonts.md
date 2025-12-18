# ``WKInternalsNotes/WKProcessPool/_registerAdditionalFonts(_:)``

追加フォント名をプロセスプールに登録する。

## Objective-C Declaration
```objective-c
- (void)_registerAdditionalFonts:(NSArray<NSString *> *)fontNames WK_API_AVAILABLE(macos(26.0));
```

## Discussion
`registerAdditionalFonts(fontNames)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L200`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L200)
- [`WKProcessPool.mm#L724`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L724)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
