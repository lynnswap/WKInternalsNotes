# ``WKInternalsNotes/_WKInspector/printErrorToConsole(_:)``

検査対象ページの JavaScript console にエラー文字列を出力する。

## Objective-C Declaration
```objective-c
- (void)printErrorToConsole:(NSString *)error;
```

## Discussion
`self.webView` に対して `console.error("...")` を評価し、指定文字列を console 出力として送る。`completionHandler` は `nil` で、結果は待たない。

## References
- [`_WKInspector.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L59)
- [`_WKInspector.mm#L200`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L200)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
