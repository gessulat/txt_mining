Results = load('resultsforplot-0mr1r.csv');

Res = {Results(Results(:,1)==0,:),Results(Results(:,1)==1,:)};
sampling_methods = cellstr(['most-referenced'; 'random']);

for k = [1:size(Res,2)]
	R = Res{k};
	sampling_method = sampling_methods{k};

	lambdas = R(:,2);
	lambda_range = intersect(lambdas, min(lambdas):max(lambdas));

	labels = [];
	cc=hsv(length(lambda_range)+5);
	color_idx = 1;
	figure;
	for lambda = lambda_range
		labels = [labels;strcat('lambda-',num2str(lambda))];
		idx = lambdas == lambda;
		plot(R(idx,3), R(idx,5), '@-','color', cc(color_idx, :));
		text(R(idx,3), R(idx,5), num2str(R(idx,4)), 'horizontalalignment','left', 'verticalalignment', 'top');
		hold on;
		color_idx = color_idx +1;
	end

	title(strcat('K-Mediods- Error for ', sampling_method));
	xlabel('r-values');
	ylabel('error');
	legend(cellstr(labels));
end

for k = [1:size(Res,2)]
	R = Res{k};
	sampling_method = sampling_methods{k};

	lambdas = R(:,2);
	lambda_range = intersect(lambdas, min(lambdas):max(lambdas));

	labels = [];
	cc=hsv(length(lambda_range)+5);
	color_idx = 1;
	figure;
	for lambda = lambda_range
		labels = [labels;strcat('lambda-',num2str(lambda))];
		idx = lambdas == lambda;
		plot(R(idx,3), R(idx,4), '@-','color', cc(color_idx, :));
		hold on;
		color_idx = color_idx +1;
	end

	title(strcat('K-Mediods- No of Clusters _', sampling_method));
	xlabel('r-values');
	ylabel('#Clusters');
	legend(cellstr(labels));
end