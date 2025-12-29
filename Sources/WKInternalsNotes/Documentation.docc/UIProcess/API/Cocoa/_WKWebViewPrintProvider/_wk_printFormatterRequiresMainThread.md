# ``WKInternalsNotes/_WKWebViewPrintProvider/_wk_printFormatterRequiresMainThread``

メインスレッド必須かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _wk_printFormatterRequiresMainThread;
```

## Default Value
`NO`。

## Discussion
`WKContentView` 実装では常に `NO` を返す。

## References
- [`_WKWebViewPrintFormatterInternal.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatterInternal.h#L47)
- [`WKContentView.mm#L1160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
