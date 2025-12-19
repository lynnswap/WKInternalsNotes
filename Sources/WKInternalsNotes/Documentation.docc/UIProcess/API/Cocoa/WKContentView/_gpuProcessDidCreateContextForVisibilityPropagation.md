# ``WKInternalsNotes/WKContentView/_gpuProcessDidCreateContextForVisibilityPropagation()``

GPU プロセスの可視性伝播コンテキスト生成を通知する。

## Objective-C Declaration
```objective-c
- (void)_gpuProcessDidCreateContextForVisibilityPropagation;
```

## Discussion
`_setupVisibilityPropagationForGPUProcess` を呼び、伝播ビューを再設定する。

## References
- [`WKContentView.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L111)
- [`WKContentView.mm#L960`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L960)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
